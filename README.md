# Elevators-offline
In this assignment we get a building with some floors and elevators, and we need to design in the best way the requests of the people that want to use the elevators.
in our input files we get csv file of all the request we need to design and the parameters of the building floors and number of elevators.

this problem is an offline, because we got all of our data, and we calculate the output before the elevator

when we search about this problem we find some idea of algorithms that we can use to find the best way to sort the calls to the elevators.
the most effective algorithm that we taught to use is the "Travelling Salesman problem"
but complexity of this algorithm is: 2^n and for a big amount of calls it will take a lot of time to find the design of the request

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


# *uml*
![image](https://user-images.githubusercontent.com/35407628/142432802-3f5cc0f9-fbe7-426f-8adf-259be1ed6d3a.png)
