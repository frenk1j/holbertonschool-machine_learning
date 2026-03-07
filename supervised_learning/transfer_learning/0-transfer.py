#!/usr/bin/env python3
"""Transfer Learning with CIFAR-10 using Keras Applications"""

import numpy as np
from tensorflow import keras as K


def preprocess_data(X, Y):
    """
    Pre-processes the CIFAR-10 data for the model.

    X: numpy.ndarray of shape (m, 32, 32, 3) - CIFAR-10 images
    Y: numpy.ndarray of shape (m,) - CIFAR-10 labels

    Returns: X_p, Y_p
    """
    X_p = K.applications.efficientnet.preprocess_input(
        X.astype('float32')
    )
    Y_p = K.utils.to_categorical(Y, 10)
    return X_p, Y_p


if __name__ == '__main__':
    (X_train, Y_train), (X_test, Y_test) = K.datasets.cifar10.load_data()

    X_train_p, Y_train_p = preprocess_data(X_train, Y_train)
    X_test_p, Y_test_p = preprocess_data(X_test, Y_test)

    input_tensor = K.Input(shape=(32, 32, 3))

    scaled = K.layers.Lambda(
        lambda x: K.backend.resize_images(
            x, 7, 7,
            data_format='channels_last',
            interpolation='bilinear'
        )
    )(input_tensor)

    base_model = K.applications.EfficientNetB0(
        include_top=False,
        weights='imagenet',
        input_tensor=scaled,
        pooling='avg'
    )

    base_model.trainable = False

    feature_extractor = K.Model(
        inputs=input_tensor,
        outputs=base_model.output
    )

    print("Pre-computing features from frozen layers...")
    train_features = feature_extractor.predict(
        X_train_p, batch_size=256, verbose=1
    )
    test_features = feature_extractor.predict(
        X_test_p, batch_size=256, verbose=1
    )
    print("Feature extraction complete!")

    feat_input = K.Input(shape=(train_features.shape[1],))
    x = K.layers.BatchNormalization()(feat_input)
    x = K.layers.Dense(
        512, activation='relu',
        kernel_regularizer=K.regularizers.l2(1e-4)
    )(x)
    x = K.layers.Dropout(0.4)(x)
    x = K.layers.Dense(
        256, activation='relu',
        kernel_regularizer=K.regularizers.l2(1e-4)
    )(x)
    x = K.layers.Dropout(0.3)(x)
    output = K.layers.Dense(10, activation='softmax')(x)

    head_model = K.Model(inputs=feat_input, outputs=output)

    head_model.compile(
        optimizer=K.optimizers.Adam(learning_rate=1e-3),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    callbacks = [
        K.callbacks.ReduceLROnPlateau(
            monitor='val_accuracy',
            factor=0.5,
            patience=3,
            verbose=1,
            min_lr=1e-6
        ),
        K.callbacks.EarlyStopping(
            monitor='val_accuracy',
            patience=10,
            restore_best_weights=True,
            verbose=1
        )
    ]

    print("Training classification head...")
    head_model.fit(
        train_features, Y_train_p,
        validation_data=(test_features, Y_test_p),
        epochs=50,
        batch_size=256,
        callbacks=callbacks,
        verbose=1
    )

    print("Starting fine-tuning phase...")
    base_model.trainable = True

    for layer in base_model.layers[:-20]:
        layer.trainable = False

    full_input = K.Input(shape=(32, 32, 3))
    x2 = K.layers.Lambda(
        lambda img: K.backend.resize_images(
            img, 7, 7,
            data_format='channels_last',
            interpolation='bilinear'
        )
    )(full_input)

    base_out = base_model(x2, training=False)

    x2 = K.layers.BatchNormalization()(base_out)
    x2 = K.layers.Dense(
        512, activation='relu',
        kernel_regularizer=K.regularizers.l2(1e-4)
    )(x2)
    x2 = K.layers.Dropout(0.4)(x2)
    x2 = K.layers.Dense(
        256, activation='relu',
        kernel_regularizer=K.regularizers.l2(1e-4)
    )(x2)
    x2 = K.layers.Dropout(0.3)(x2)
    final_out = K.layers.Dense(10, activation='softmax')(x2)

    final_model = K.Model(inputs=full_input, outputs=final_out)

    trainable_types = (
        K.layers.Dense,
        K.layers.Dropout,
        K.layers.BatchNormalization
    )
    head_layers = [
        lay for lay in final_model.layers
        if isinstance(lay, trainable_types)
    ]
    head_model_layers = [
        lay for lay in head_model.layers
        if isinstance(lay, trainable_types)
    ]
    for fl, hl in zip(head_layers, head_model_layers):
        fl.set_weights(hl.get_weights())

    final_model.compile(
        optimizer=K.optimizers.Adam(learning_rate=1e-5),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    ft_callbacks = [
        K.callbacks.ReduceLROnPlateau(
            monitor='val_accuracy',
            factor=0.5,
            patience=3,
            verbose=1,
            min_lr=1e-7
        ),
        K.callbacks.EarlyStopping(
            monitor='val_accuracy',
            patience=8,
            restore_best_weights=True,
            verbose=1
        )
    ]

    final_model.fit(
        X_train_p, Y_train_p,
        validation_data=(X_test_p, Y_test_p),
        epochs=20,
        batch_size=128,
        callbacks=ft_callbacks,
        verbose=1
    )

    final_model.save('cifar10.h5')
    print("Model saved as cifar10.h5")

    loss, acc = final_model.evaluate(
        X_test_p, Y_test_p, batch_size=128, verbose=1
    )
    print(f"Final Test Accuracy: {acc:.4f}")
