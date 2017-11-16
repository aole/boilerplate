'''
https://www.tensorflow.org/install/
'''

import numpy as np
import tensorflow as tf

__author__ = 'Bhupendra Aole'
__version__ = '0.1.0'

# create a session to run the operations
sess = tf.Session()

# static tensors
t1 = tf.constant( 3. )
t2 = tf.constant( 4. )
tr = tf.add( t1, t2 )
# run the session
print( sess.run( tr ) )

# parameterized tensors
t3 = tf.placeholder( tf.float32 )
t4 = tf.placeholder( tf.float32 )

# operations on tensors
tr = t3 * t4
res = sess.run( tr, { t3: 5., t4: [6., 7.] } )
print( res )

# variable inputs, tf will update these when trained
m = tf.Variable( [.3], dtype = tf.float32 )
b = tf.Variable( [-.3], dtype = tf.float32 )

x = tf.placeholder( tf.float32 )
linear_model = m*x + b

# need to initialize variables
init = tf.global_variables_initializer()
sess.run( init )

x_train = [1, 2, 3, 4]
print( sess.run( linear_model, {x: x_train } ) )

# linear_model returns output given variables m and b
# if the desired output is different, we need to adjust m, b

# desired output
y = tf.placeholder( tf.float32 )
y_train = [0, -1, -2, -3]
squared_deltas = tf.square( linear_model - y )
# loss function (this is essentially how far away are we from output)
loss = tf.reduce_sum( squared_deltas )
print( sess.run( loss, {x: x_train, y: y_train } ) )

# if we use x=-1 and b=1 we get the desired output
fixm = tf.assign( m, [-1.] )
fixb = tf.assign( b, [1.] )
sess.run( [fixm, fixb] )
# run the same loss function as before, but this time we get loss=0
print( sess.run( loss, {x: x_train, y: y_train } ) )

#
# *** MACHINE LEARNING ***
# we can train the model to come to the correct values for our linear variables
#

optimizer = tf.train.GradientDescentOptimizer( .01 )
train = optimizer.minimize( loss )

sess.run( init ) # reset values to incorrect defaults.
currm, currb, currloss = sess.run( [m, b, loss], {x: x_train, y: y_train} )
print( 'Before training m:%s b:%s loss:%s'%( currm, currb, currloss ) )

# *** TRAIN ***
for i in range( 1000 ):
    sess.run( train, {x: x_train, y: y_train} )

currm, currb, currloss = sess.run( [m, b, loss], {x: x_train, y: y_train} )
print( 'After training m:%s b:%s loss:%s'%( currm, currb, currloss ) )

#
# tf.estimator
#

feature_columns = [tf.feature_column.numeric_column( 'x', shape=[1] )]

estimator = tf.estimator.LinearRegressor( feature_columns = feature_columns )

x_train = np.array( [1., 2., 3., 4.] )
y_train = np.array( [0., -1., -2., -3.] )
x_eval = np.array( [2., 5., 8., 1.,] )
y_eval = np.array( [-1., -4., -7., 0] )

input_fn = tf.estimator.inputs.numpy_input_fn(
    {'x': x_train}, y_train, batch_size=4, num_epochs=None, shuffle=True )
eval_input_fn = tf.estimator.inputs.numpy_input_fn(
    {'x': x_eval}, y_eval, batch_size=4, num_epochs=1000, shuffle=True )

estimator.train( input_fn = input_fn, steps = 1000 )

eval_metrics = estimator.evaluate( input_fn = eval_input_fn )
print( 'metrics: %r'%eval_metrics )
