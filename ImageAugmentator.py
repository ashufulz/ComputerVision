import cv2, os, imutils, random
import numpy as np
import imgaug.augmenters as ia


# -------------------------------------------------------
# VARIABLES
IMG_FOLDER = r'C:\Users\AshutoshFulzele\PycharmProjects\AshProjects\Assets\Images\TrafficLights'
AUG_IMG_FOLDER = r'C:\Users\AshutoshFulzele\PycharmProjects\AshProjects\Assets\Images\Augmented_TrafficLights'

LIGHTS = ['Red', 'Green', 'Yellow']                     # pre-defined names of folders in which augmented images would be stored
IMAGES = []                                             # to store paths of images from that respective image folder

TOTAL_IMAGES = 6000                                     # total number of images to be augmented per folder
i = 1
# -------------------------------------------------------


""" Augmentation Functions to be performed on an image """
def flip_h(image):
    """ Flips an image on Vertical axis (left - right) """
    return np.fliplr(image)


def rotate(image):
    """ Randomly rotates the image in range of -20 degrees to +20 degrees """
    return imutils.rotate(image, random.randint(-20, 20))


def noise(image):
    """ Randomly generate Noise in the image data """

    # Gaussian Noise
    gaussian = ia.AdditiveGaussianNoise(loc=0, scale=0.1*255).augment_image(image)

    # Poisson Noise
    poisson = ia.AdditivePoissonNoise(lam=10, per_channel=True).augment_image(image)

    # Salt and Pepper Noise
    saltPepper = ia.SaltAndPepper(p=0.05).augment_image(image)

    # Appending them all in a list
    noise = [gaussian, poisson, saltPepper]

    return random.choice(noise)


def weather(image):
    """ Randomly add Weather conditions to an image """

    # Adding Snowflakes environment
    snowFlakes = ia.Snowflakes(flake_size=(0.1, 0.4), speed=(0.01, 0.05)).augment_image(image)

    # Adding Rain
    rain = ia.Rain(speed=(0.1, 0.3)).augment_image(image)

    # Adding Foggy weather
    fog = ia.Fog().augment_image(image)

    weather = [snowFlakes, rain, fog]

    return random.choice(weather)


if __name__ == '__main__':
    while True:
        # Appending all the above functions into a dictionary
        augmentations = {
            'flip': flip_h,
            'rotate': rotate,
            'noise': noise,
            'weather': weather
        }

        for light in LIGHTS:
            for im in os.listdir(os.path.join(IMG_FOLDER, light)):                  # read image name from folder and append its path into "IMAGES" array
                IMAGES.append(os.path.join(IMG_FOLDER, light, im))

            while i <= TOTAL_IMAGES:
                aug = random.choice(list(augmentations))

                image = random.choice(IMAGES)
                image = cv2.imread(image)

                image = augmentations[aug](image)

                image = cv2.resize(image, (128, 128))

                AUG_IMG_PATH = r'{}\{}\Aug_{}_{}.jpg'.format(AUG_IMG_FOLDER, light, light, i)
                cv2.imwrite(AUG_IMG_PATH, image)

                i += 1

                if i == TOTAL_IMAGES:
                    print(light+' DONE')

            IMAGES.clear()                                                          # Flushing out the list
            i = 1                                                                   # Resetting the iterator

        break

cv2.destroyAllWindows()
