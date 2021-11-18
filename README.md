# Elevators-offline
In this assignment we get a building with some floors and elevators, and we need to design in the best way the requests of the people that want to use the elevators.

in our input files we get csv file of all the request we need to design and the parameters of the building floors and number of elevators.

this problem is an offline, because we got all of our data, and we calculate the output before the elevator

when we search about this problem we find some idea of algorithms that we can use to find the best way to sort the calls to the elevators.
the most effective algorithm that we taught to use is the "Travelling Salesman problem"
but complexity of this algorithm is: 2^n and for a big amount of calls it will take a lot of time to find the design of the request

so we choose to use a "greedy algorithm" that find for the request what is the closest elevator to take this call.

this is the main source that we learn about this problem:
1. https://thinksoftware.medium.com/elevator-system-design-a-tricky-technical-interview-question-116f396f2b1c - elevator system design from medium
2. https://www.youtube.com/watch?v=xOayymoIl8U&ab_channel=SpanningTree - youtube videos that sum veriaty of algoritems for elevetors
3. https://www.youtube.com/watch?v=JXqVvmBOyyQ&ab_channel=Intertent - another youtube video about elevator design.


*Our code*

In our code we scan over the time from the first call to the last with a function we call cmd.
and for every call we check what is the best elevator that answers it, we calculate it with the calls that the elevators already contain and this call too and consider the direction of the elevator calls.

We use a priorityQueue to save the floor of the calls for every elevator.
