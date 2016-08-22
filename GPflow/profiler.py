import tensorflow as tf
import session

def activateTracer(outputFileName,outputDirectory=None,eachTime=False):
	session.setSession( session.TracerSessionFactory(outputFileName,outputDirectory,eachTime) )

def deactivateTracer():
	session.setSession( tf.Session )