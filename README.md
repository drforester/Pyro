![alt text][image0]

[//]: # (Image References)
[image0]: ./images/conflag.gif
[image1]: ./images/0000.png
[image2]: ./images/0134.png
[image3]: ./images/0605.png  


# Pyro   
Pyro is a simulated, 2D world comprised of cells of 5 types. The interaction of neighboring cells can exhibit interesting patterns. The possible cell types are:

```
0 : Empty
1 : Defender
2 : Mine
3 : Metamorph
4 : Invader
```

Hopefully the reasons for the cell names will be obvious when you study the interaction rules in the program pyro.py. It's possible though that I let my imagination run a bit too far and that better names could be assigned.  


### About  
Maybe the red cells (the invaders) represent fire spreading in a forest, maybe they represent a disease spreading in the host's body, maybe they are a particularly fecund species of red bunny, maybe in our world there lives a happy little tree over there.... wait, sorry. The groups of red cells are not guaranteed to grow. In fact, with smaller world maps, it can be seen that the invaders are not always able to overwhelm the defenders. Each cell is assigned a type at runtime, so if you run the program and the "fire" does not appear to spread, then restart as many times as necessary (usually just once or twice) until conditions are favorable. Eventually "flames" will touch all cells, meaning that the "conflagration" lives on forever, or at least until the condition of the while loop is met or the user enters Ctrl+C and the program halts.

The world map should initially resemble this:  
![alt text][image1]  

After some dozens of iterations, large groups of red cell may form:  
![alt text][image2]  

Finally, the world will be engulfed in swaying shoals of red cells:  
![alt text][image3]  



If you are interested enough to clone this repository and to run the program, then please experiment with the rule-set. Small changes can make a great difference. If you tease out any interesting behavior, please share your rule-set with me so I can try it.