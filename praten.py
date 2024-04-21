import tensorflow as tf
#print(tf.version)


rank1_tensor = tf.Variable(["Test"], tf.string)
rank2_tensor = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)

#print(tf.rank(rank2_tensor))

t =tf.zeros([5,5])
print(t)