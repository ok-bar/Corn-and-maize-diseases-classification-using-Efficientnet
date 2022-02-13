def scheduler(epoch, lr):
  if epoch < 3:
    return lr
  else:
    return lr * tf.math.exp(-0.1)

def callbacks(patience=2):
  checkpoint = tf.keras.callbacks.ModelCheckpoint('my_model.h5', monitor='val_loss', verbose=1, save_best_only=True, save_weights_only=True)
  early=tf.keras.callbacks.EarlyStopping(monitor='val_loss',patience=patience,min_delta=0.001)
  lr=tf.keras.callbacks.LearningRateScheduler(scheduler)
  callbacks_list=[checkpoint, early,lr]
  return callbacks_list
