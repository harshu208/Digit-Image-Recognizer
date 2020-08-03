# Digit-Image-Recognizer
<p>Simple real time digit recognition application developed in python, where user draws a digit in the GUI and application predicts the drawn digit.</p>
<ul>
  <li>Training data and test data are loaded using mnist dataset provided by keras. Then the data is reshaped to the shape which is our model expects while training.</li>
  <li> CNN sequential model is created and compiled.</li>
  <li>The model is trained on the training data and the trained weights is stored in a file named 'mnist.h5'</li>
  <li>An interactive window is created using python Tkinter library.</li>
  <li>The testing image should have digit in white and rest all background as black.</li>
  <li>Load the pretrained model weights and use it on image to predict the digit.</li>
  </ul>
