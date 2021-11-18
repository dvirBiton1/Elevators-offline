# Elevators-offline
In this assignment we get a building with some floors and elevators, and we need to design in the best way the requests of the people that want to use the elevators.
in our input files we get csv file of all the request and the parameters of the building floors we need to design it in the best way.

this problem is an offline algorithem problem, because we got all of our data before, and we calculate the output for the future action od the elevator

# our reaserch
when we search about this problem we find some idea of algorithms that we can use to find the best way to sort the calls to the elevators.
the most effective algorithm that we thought to use is the "Travelling Salesman problem"
the complexity of this algorithm is: 2^n and for a big amount of calls and elevators it will take a lot of time to find the design of the request.
<br> 
so we choose to use a "greedy algorithm" that find for the request call what is the closest elevator that will take this call the fastest.
<br>

# this is the main source that we learn about this problem:
1. https://thinksoftware.medium.com/elevator-system-design-a-tricky-technical-interview-question-116f396f2b1c - elevator system design from medium
2. https://www.youtube.com/watch?v=xOayymoIl8U&ab_channel=SpanningTree - YouTube videos that sum verity of algorithms for elevators
3. https://www.youtube.com/watch?v=JXqVvmBOyyQ&ab_channel=Intertent - another Youtube video that explain the different method of how to use elevators


# Our code

In our algorithm we scan over every second from the first call to the last and see if there is a new call for this time.
if we have new call we search elevators that will pass this floor in its action or elevators that have no calls to answer at all.
we save this potential elevators and find the best elevator of them that will take this call the fastest.
if there is some calls in the same second we choose the right elevator to the calls and then moving second ahead.

1. we scan for every second if there is a new call in the building
2. if we have a new call - we update the location of each elevator and it's parameters about its direction and next floor
3. the program choose the elevators that potentials to complete this call fast 
4. from this group of elevators we find in step 3, we calculate the fastest call that will answer about this call
5. we update the new value of the chosen elevator with the new call it can be answer
6. we check if there are more calls to answer. if there isn't - we continue to move the time forward


# *uml*

![Uml](https://user-images.githubusercontent.com/35407628/142432892-1a4e34bf-bc48-4258-85bd-465122c5a0e7.png)
