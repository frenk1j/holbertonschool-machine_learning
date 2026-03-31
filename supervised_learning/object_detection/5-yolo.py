def preprocess_images(self, images):
    """Preprocess images for input to the Darknet model.

    Resizes images with inter-cubic interpolation and rescales pixel
    values to the range [0, 1].

    Args:
        images: list of images as numpy.ndarrays

    Returns:
        tuple of (pimages, image_shapes):
            pimages: numpy.ndarray of shape (ni, input_h, input_w, 3)
            image_shapes: numpy.ndarray of shape (ni, 2)
                containing original height and width of each image
    """
    input_h = int(self.model.input.shape[1])
    input_w = int(self.model.input.shape[2])

    pimages = []
    image_shapes = []

    for image in images:
        image_shapes.append(image.shape[:2])

        resized = cv2.resize(
            image,
            (input_w, input_h),
            interpolation=cv2.INTER_CUBIC
        )

        # BGR → RGB
        resized = resized[..., ::-1]

        # Normalize to [0, 1]
        resized = resized / 255.0

        pimages.append(resized)

    pimages = np.array(pimages, dtype=np.float32)
    image_shapes = np.array(image_shapes)

    return pimages, image_shapes
