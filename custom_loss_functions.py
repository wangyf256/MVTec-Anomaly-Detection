import tensorflow as tf
from tensorflow import keras
import keras.backend as K


def ssim(img_true, img_pred):
    return (1 - K.mean(tf.image.ssim(img_true, img_pred, 1.0), axis=-1)) / 2


def mssim(img_true, img_pred):
    return 1 - K.mean(tf.image.ssim_multiscale(img_true, img_pred, 1.0), axis=-1)


def l2(img_true, img_pred):
    return 2 * tf.nn.l2_loss(img_true - img_pred)


# https://www.tensorflow.org/api_docs/python/tf/nn/l2_loss?hl=ko

# --------------------------keep this as backup--------------------------------
# max_value = 1.0
# def custom_loss(max_value):
#     def loss(y_true, y_pred):
#         return tf.image.ssim(img1=y_true, img2=y_pred, max_val=max_value)

#     return loss

# loss=custom_loss(max_value),
# metrics=[custom_loss(max_value)],
# -----------------------------------------------------------------------------


# --------tested, works on specific object classes and fails on others---------
# def ssim_loss(y_true, y_pred):
#     return -1 * tf.reduce_mean(tf.image.ssim(y_true, y_pred, 1.0))
# -----------------------------------------------------------------------------
