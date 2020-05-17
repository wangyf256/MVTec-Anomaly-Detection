import tensorflow as tf
from tensorflow import keras
import keras.backend as K


def ssim_metric(dynamic_range):
    # return (K.mean(tf.image.ssim(imgs_true, imgs_pred, 1.0), axis=-1) + 1) / 2
    def ssim(imgs_true, imgs_pred):
        return K.mean(tf.image.ssim(imgs_true, imgs_pred, dynamic_range), axis=-1)

    return ssim


def mssim_metric(dynamic_range):
    def mssim(imgs_true, imgs_pred):
        return K.mean(
            tf.image.ssim_multiscale(imgs_true, imgs_pred, dynamic_range), axis=-1
        )

    return mssim