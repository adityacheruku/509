'''Solo Rider
Problem Description
Alex is a freelance developer, who develops applications. One day he got a proposal to develop an app called "SoloRider" which is a transportation service within Hyderabad city.

Lets consider a location Hyderguda within the city. When a passenger gets down at this location, then the vehicle should be assigned to the nearest customer who booked the transportation service. But there will be multiple customers who booked the service and there will be multiple vehicles which will be available to serve that request, in the vicinity. So Alex needs to develop an application which will allocate passengers to the appropriate vehicles. His application will calculate the coordinate points of all the passengers and vehicles in the given area and then it follows the below rules to do passenger to vehicle assignment.

Given N passengers and M vehicles which are idle at the given time in Hyderguda. You will have to assign one vehicle to each passenger based on the given rules.

The customers should be prioritized based on the lexicographical order of their names.
For a given customer, allocate the nearest vehicle which is idle. Here the term idle indicates that the vehicle is currently not associated with any passenger. Use Manhattan Distance for measuring distance between passenger and vehicle, vice versa.
If more than one idle vehicle are equidistant from the passenger, then allocate them the vehicle which is lexicographically closest.
Vehicles have vehicle numbers in the format vid where id is an integer. Lexicographically closest means the one which comes first in the alphabetical order.
Once a vehicle gets allocated, then it will move towards the passenger and is no longer available to any other passenger.
Print the minimum distance traveled by all the vehicles to reach their passengers obeying the given rules.

Constraints
1 <= N, M <= 100

1 <= x,y coordinates <= 10^3

Name of the passenger always comprises or upper and lower case characters.

Vehicle number is in the format "vid" where id is an integer.

Number of passengers <= Number of vehicles.

Input
The first line consists of two space delimited integers N, M denoting the number of passengers and vehicles.

Next N lines will consist of the passenger's name and x,y coordinates of the passenger's exact location, all delimited by space.

Next M lines will consist of the vehicle's number and x,y coordinates of the vehicle's exact location, all delimited by space.

Output
Single line consisting of an integer denoting the minimum distance traveled by all the vehicles to reach their passengers obeying the given rules.

Time Limit (secs)
1

Examples
Example 1

Input

4 8

Vishnu 4 4

Ravali 1 6

Krishna 8 3

Vaishnavi 3 2

v106 6 4

v42 2 4

v69 4 1

v45 3 3

v66 5 3

v312 9 5

v93 8 1

v123 4 6

Output

8

Explanation

By plotting the given coordinate points in the 2d graph, it looks like below.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@407cf41:image1.png
According to the rules, we prioritize the customers in lexicographical order of their names. So we try assigning a vehicle to the customer named Krishna. For Krishna, the nearest vehicle is v93, so we will assign that vehicle to him. For Ravali, the vehicles are v42, v123 are at a distance of 3 from her. So we will assign the one which comes lexicographically first i.e., v123 will be assigned to Ravali. For Vaishnavi, v45 is the nearest vehicle. So we will assign her to that vehicle. Lastly, for Vishnu, v123, v42, v106, v45, v66, all these vehicles are at a distance of 2 from him. Since v123, v45 are already allocated and they are on the way to their customers, we exclude them. Thus we allocate v106 to Vishnu.

On calculating the total distance traveled by all the vehicles in order to reach their customers, the output is 8.

Example 2

Input

3 5

Maya 4 4

Neha 1 1

Tara 7 1

v11 3 6

v82 1 6

v69 4 1

v109 3 3

v26 10 5

Output

12

Explanation

By plotting the given coordinate points in the 2d graph, it looks like below.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@407cf41:image2.png

According to the rules, we prioritize the customers in lexicographical order of their names. So we try assigning a vehicle to the customer named Maya. Nearest vehicle to Maya is v109 and we will assign that to her. For Neha, The nearest is v69, so we will assign v69 to Neha. Lastly, for Tara, we will assign v26.

On calculating the total distance traveled by all the vehicles in order to reach their customers, the output is 12.
'''