
# **<p align=center>SHAPE-PLOT</p>**

big dreams, for his project.<br>
to start with, a GUI with input for panel sizes and then rill it with non overlaping circles.

</p>

---
## **CHANGELOG**</p>


v0.0 - the begining
v0.1 - the begining, but with a little bit more code


</p>

---
## **ROADMAP**</p>


- collision detection with circles.
- draw other polygons, rotateable.
- collision detection with the other polygons

</p>

---
## **DEVLOG**</p>

- so from what i can see, tkinter will be the best chooice for what i want to do, after i ger a window, im lost.
</p>

- got a window, with a 'canvas', click the mouse and it plots circle of a random size. currently figuring out how to implanemt colision detction. when there are jus2 circles its easy, but as soom as i add another one my method doesnt work. i think i need to treat the shapes as growing into position. I will start again, taking waht i have learnt so far, and get the circles to grow to there values, checking to see if they are hitting there neibours.
</p>

- so im trying to join two different tutorials that i found online, problem is they use different was to init the classes, and this is the first OOP i have ever tried to write. however, i did manage to get a circle that grows.... but it doesnt refresh and kees the old circle as well, and it can only grow one at a time, but its a start. going to bug out on this and do some OOP stuff so i have a better grip on it.
</p>

- OOP is pain. ok, got a circle that refreshes, and grows, can only do one at a time, all good though. now i want to get it to stop growing when it hits another circle
</p>

- ok, i think i can make it stop, but before i get to far i will throw some button in there to set the size and play with some settings of the window and shape. also, i think at the moment im wasting my time with OOP, im just using it like a function call because its only triggering one output, will stick with it though, its fin learning.
</p>

- ok,ok,ok, i think i found the first parctical use for OOP that i have come across. so i want to change the canvas size from a different frame. but i dont have the canvas object in the funtion i am using, in OOP i could make a method that would return the cavvas name so i could use it, i dont know if this is right, but it is facanating to think about.
</p>

- aaaaaannnnnd, now i rewrite it to accomadate for buttons. 
</p>

- ok.. so putting it into classes wasnt that hard. but now i think i dont need it. problem i have is that the size of the canvas class depends on the size's typed in the menu class, and when i type something in the menu class i want it to update the canvas class, but i cant (dont know how to) make it work both ways. from waht i understand, oop is all about inheratance, and passing shit between classes like this is bad, so i should have a different heirachy.... at the moment this seems very liner so i think i will go back to a functioanl way of doing things for the moment, pretty sure that i can solve my earlier problems with what i have learnt.  
</p>

- what a mindfuck. hindsight is 20/20... theh problem with trying to solve a problem you know nothing about is that you can end up fucking with shit that has nothing to do with the problem. That being said, i leart a shit load along the way.<br>
i now have entry boxes, and a button that can change the size of the canvas.<br>
only took 3 days, now that i know i can control the canvas through i can keep going... kinda lost where i was to be honest, thats right circles.
</p>

- before i move back onto the collision detection i will fix up the Grow calss. i can see its a mess now and may as well be a function however, i would still like it to be a class, but create other shapes, not just circles. 
</p>

- ok, fixing the grow class.. welll... making a new class to put shapes on, i can see why there is a lot of talk anout knowing the structure of a program before you start writing it. i know what i want the program to do right now, but i also know what i want it to do later, and i want to write it so i can add the latter with as little modification to the base code as possible. i guess it comes with experence, and i have none. so im constantly running through variations in my head that i dont know the answer too, while staring at the screen doing nothing.  
</p>

- so now i have squares, circles, and tiangles placed at random, fun times. still got other shapes, then have options for altering the orentation, then have options for alterign the size, then be able to add with mouseclick, thhen collision dection, then the rest of the crazy shit. this will be fun. 

- shit i didnt think about. shapes are different sizes with they have the same lenght edges
<p>

- trying to implament a sub frame to control the size of the shapes, taking a bit more time than i thought it would, mainly becaus i know nothing about how to do what i want, only what i actualy want. it seems like every time i learn something, there is somethhing that i did two steps ago that can be improved with my new knowlage. So i am taking a few steps back and trying to figure out pack/place/grid. so far i have been using grid, and its just been working out, but i tried to set the size of a frame to a fized value and its not working. i dont plan on making a polished UI straight away, but i would like to not make a giant mess that ends up breaking thinga later on, so i will take a bit of time now.
</p>    

- really glad i done that, what a pain to srt it out now, would have only got worse. all in all, very much like html frames. going back to try to get the size and rotation frames setup complete, then implement the functionality.

- started thinking a couple of steps ahead of what i am currently doing in the hope of saving a little bit of time, by not having to rewrite code. size and rotation frames are set, and values are passed to the shape function, but the generate function will only work with random values, and i want to be able to click the canvas too, and im a bit lost as to how to get the values from the subframe to the canvas frame. im begining to think that putting the frame generation in a function might have been a bad idea. if it was in a class i could possibly write a method to return the values of the menu? maybe? i might just have to writer another function.... just had a thought, just a dictionary at the start of the program that stores all the values of the menu, that way i can write a function that will return the values of the dictionary. i will try this, as i can see it it will be a simple solution.  


- i think i am over complicating this. if this was in one program, and the mainloop was not in a function, then the variables woudl be easy to acess from any widget.... it would be a huge program, and maybe hard to read, but i wouldnt have to make workarounds for simple problems. i dont think OOP would help, time to rewrite. not quite rewrire, but incorpparate the functionality of the side menu into the main program and remove the name === __main__ function call.

- but you know, im going to over think this again, it wuoudl be great ti use OOP so i think i will put he menus into classes? is this a good idea? i dont know. as long as i can change global dicts from inside a calss function i dont see a problem, it will make the code a bit easier to read, as will be able to colapase the classes. i will test with the bottom menu, as it uses a dict for the width and height.

- so dict values are changed from inside a class, thats good to know. i cant see any drawbacks yet for doing it this way, there will be some, i just cant see them yet. more than likley i will have to change my code again later on when i hit an impossible wall.

- the cycle continues. In order to save myself from writing confusing code thats hard to read, i wrire confusing code thats hard to read. love it. i still feel that in the long run this will be more adapatable. i do laugh/cry about how many times i have flip floped between functional and OOP.

- bypassed the grow class at the moment, however, i have managed to get to get clicking on the canvas, and the button in the right menu to work as intended. it was easy once everthing was in place. after i put everything in classes, i realised i didnt need to have dict values to hold onto the values in the right menu, i can just have a method that retrives them, this makes calling size/shape/angle easy to get from anywere. i wonder if i was learning this in any kind of formal setting if i would pick up on this kind of stuff earlier.. would i be learing as much about *how* it works. i wonder if i am even learing it right.....

- making progress, dont know if its good, will probably have to rewrite stuff when i add more functionality. can make shapes at any size, and at any angle, either by clicking the position on the canvas or random placement. a clear canvas button would be great, ill work on that too, also just being able to remove indervidual elements would be good too, and maybe the last elemnt made. lots to do.  

- thinking ahead again... if i want to be able to select and delete elemnets in the canvas, i may need to change the way that i am drawing the shapes. will look into this.

- you know when you think that there is a problem that will be really hard to solve so you dont even look at it. then you have to, and its easy.. thats what its like selecting shapes on the canvas, one line of code, built in function, love it. i still think i may need to change the way that i am adding shapes, as i think that the shapes are in different instances of the class, and it would probably be benificial to me if they were in the same instance 

- i love how somtimes i think that the code i write moghth take a while to run, then i test it, and it can do 5 million itterations in under 1 second. 

- at another one of those roadblocks where im not sure what piece of the puzzle i shoudl do next, so i do nothing..... im not happy with the structure of the code, it seems to jump around alot, kind of haphazardly, 

- changed the structure of the code to make it easier to read. found a code snipet online after a bit of searching, that *partialy* does what i want, separating axis theorem. works for the points of any 2 convex polygons, and returns a true/false if thhey overlap. i know how SAT works, but i would be lying if i said i knew how the code is working it out, thats a plan for another day. only *partialy* works, because now i have to figure out how far to move the shape to avoid contact. also need to figure out if i can modify the code for a circle, or if i need to rurn the circle into a giant polygon.   

- sat will work with a circle polygon combo, so thats all good. but now i need to figure out how the code works so i can implement it.

- so after reading the code im pretty sure if i feed the SAT code a mirroed polygon of matching shape, insted of a circle, it will work.  

- dear god i think it works, now to do some research. i know that the shapes collide, and need to move. so do i brute forece it, eg small.move>>check>>repeat. or do i find the maths to out the corrent direction/distance and do it in one hit. as far as ease for me bruteforce would be the best option, im nit sure how it would worl in the long run though..

- did the brute force method, with varing results. going to pause for a bit on this and work on a clear button, partly because i need a break from maths, partly because at the moment i have to restart the program when the canvas becomes to crowded.
 
- dear god i dont think it works. started left menu, but i dont think the mirroed polygon thing works...... naaaaa, it doesnt works for approx 30% of the shape, fucks out on the corners. will have to go back rework it. i know its possible, i just need to understand the program a bit better. basically for every vector it makes for the polygon i need it to make one +/- the centrepoint of the circle. prettymuch need to make a duplicate copy. something for later, gonna have a break and go back to the left menu.

- basic left menu functionality implamented, delete last, and delete all. lots more to add in the future,s but somehow i completly broke the colision functionality.....

- ok, so i think i may have found a problem for wht the collision detectin wasnt working perfectly last time, i was only adding the OG centre point to the pointlist, not the updated one. all good though, just need to do a bit of magic.

- ok, back to where i was.

- i love the fact that im learning more maths. i think i am gettign the hang of the sat function, and how it acually works. i had one try at modding it, it didnt work correctly, but now i know why. now its just a matter of getting the corrent vectors and verticies for a circle. lol.

- from the point of giving up, to sucess in about 30 seconds. im pretty sure i got it. just need to clean up the (remove the millions of print() statements) and then test. 

- so i thought i would clean up my code a little bit so i dont spend so much tome repeating stuff, i think i will have to put the sat into the shapre class, i was going to do it anyway, but i wanted to test it first. confidince is high....... it should not have been. functionality is broken.. i am broken....

- note for future me, stat at the begining when debugging. was very close to digging into the SAT code again when i realised that the input function was wrong. works now as intended. there is a divide by zero error whenever the shapes are in line, once i have the single collision move sorted i will work on fixing that.

- single collision workig, looking for a fix for div0. i thikn i may have to rewrite this code.. again. <br> currently, i am getting buddies then checking if the is 1, 2, 3 or more collisions, then altering the action taken based on that. problem is, after the action is complete, i will need to check if it has pushed the shape into colision with differernt buddies. then start the process agian. i think that a bette way might be to get the buddies, and loop through the shift values if a colision is detectd. this would also save repeating code, because, it will use the same process everytime something is placed. i think it will be more cpu intensive but its not that heavy of a program anyway.  

- holy shit, it was a little bit easy to rewrite the code, and it looks clean, and is short. still have the div0 problem, and now i need to shrink the shape when it gets caught between 3 shapes, but i feel that should be pretty easy.

- fixed div0, found a problem where a shape is not considered a buddy, but it still intersects, liks like it will happen the most with triangles, because they protrude so far from the centre.

- added variable control for hitlist length, this at the moment this is soring out the previous problem, but it might not work when i start shrinking the shapes.... and im about to do that.

- that was also relitily easy, it is slow, but considering that i know what it is doing, i think its ok. not sure what step to take next. so much i want to do.

- taking a break from the maths side of this and working on sorthing a little bit more functionality, will start with a status bar, and trying to get the prog to resize properly.

- in order to get the resize working i need to change the way the canvas is displayed, from what i understand, i will make the canvas bigger, and the only display what fits in the screen. i will add a box for the size of the 'panel', have to figure out how to not delete it though when clear all. this should be a bit of fun. fun in the way that its problem solving without looking at shapes and algebra all day.

- im at a point where i feel i need to know more about how to use classes. learning alone is hard, becaue i can make it work, but i dont know if i am doing it right i think i will watch a few videos on it. also might take a break from this and do somethin pointless, like make a snake game.




 




        











</p>    
</p>

