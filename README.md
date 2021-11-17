# Elevators-offline
In this assignment we get a building with some floors and elevators and we need to design in the best way the requests of the pepole that want to use the elevetors.

in our input files we get csv file of all the request we nees to design and the parameters of the building floors and number of elevators.

this problem is an offline, because we got all of our data, and we calculate the output before the elevator 

when we search about this problem we find some idea of algorithms that we can use to find the best way to sort the calls to the elevators.
the most effective algorithm that we tought to use is the "Travelling Salesman problem"
but complexity of this algorithm is: 2^n and for a big amaount of calls it will take a lot of time to find the design of the request

so we choose to use a "greedy algorithem" that find for the request what is the closest elevator to take this call.

this is the main source that we learn about the problem:


*Our code*

In our code we scan over the time from the first call to the last with a function we call cmd.
and for every call we check what is the best elevator that answers it, we calculate it with the calls that the elevators already contain and this call too and consider the direction of the elevator calls.

We use a priorityQueue to save the floor of the calls for every elevator.
