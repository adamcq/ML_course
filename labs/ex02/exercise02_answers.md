# Answers to the questions in EXC02

## Exercise 1
- What does each column of X ̃ represent?
  - a feature\
- What does each row of X ̃ represent?
  - a person\
- Why do we have 1’s in X ̃ ?
  - an offset weight\
- If we have heights and weights of 3 people, what would be the size of y and X ̃ ? What would X ̃ 32 represent?
  - y.shape = (3,1) X.shape = (3,2)\
- In helpers.py, we have already provided code to form arrays for y and X ̃ . Have a look at the code, and make sure you understand how they are constructed.
- Check if the sizes of the variables make sense (use functions shape).
  1. Now we will compute the MSE. Let us introduce the vector notation e = y − X ̃ w, for given model parameters $w = [w0, w1]⊤$. Show that the MSE can also be rewritten in terms of the vector e, as $L(w) = ... (4)$ 

  2. Complete the implementation of the notebook function compute loss(y, tx, w). You can start by setting w = [1, 2]⊤ , and test your function.