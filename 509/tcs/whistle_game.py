''' 
Whittle Game
Problem Description
You and your friend were playing a whittle game using a rubber band where you have a bunch of nails hammered onto a wooden board, and you encompass all the nails with the help of a rubber band by fixing it on just the exact number of outermost nails that are enough to encompass all nails.

The diagram below shows a rubber band tied around the outermost nails such that all other nails are enclosed by that shape.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@4b21844c:image1.png

After you have created the outline using the rubber band you start playing the game. Here you start by removing that nail (amongst existing nails to which rubber-band is attached) that makes the area of enclosure the minimum. In your turn, you can remove one or more nails up to a maximum number of nails as specified in the input.

The one who removes a nail such that the enclosed area becomes zero, wins the game. Assume each player removes the nail(s) in an optimal way without making any mistakes or giving any chance to let the other player win.

Note: If there are two nails, such that after its removal have the same area of the enclosure, then the one which is the bottom-most (whichever has the lowest y-coordinate), should be removed. If both have same y-coordinate, then remove the one which is left-most.


Your task is to find the nails that need to be picked to make the area of enclosure zero. Assume that you start picking up the nails first, predict if you can or cannot win the game.

Constraints
4 <= N <= 200 (such that the area enclosed by rubber-band > 0)

-10^2 <= x, y <= 10^2

1 <= m <= 100

Input
The first line contains an integer N which specifies the number of nails.

Next N lines contains the (x, y) coordinates of a nail as 2 space delimited integers.

Last line consists of single integer m which denotes the number of nails either player can pick in their turn.

Output
Print the (x, y) coordinates of the nails picked in sequential order, one on each line as 2 space delimited integers.

Last line of output should be a YES or NO indicating if the game can or cannot be win with optimal play.

Time Limit (secs)
1

Examples
Example 1

Input

6

0 0

0 4

-4 0

5 0

0 -6

1 0

2

Output

0 -6

0 4

YES

Explanation

Consider the following diagram:

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@4b21844c:image2.png

The nails have been plotted in the form of points and the rubber band is the outline made along the outermost nails.

Now you must remove the nails one by one based on the given limit, 2 in this case.

Either player can remove one nail or two nails in their turn. After removing first nail the rubber band will take the following shape:

Initially the area is 45.0.

After removing the nail (0, -6) minimum area is obtained and the shape is as depicted below

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@4b21844c:image3.png

The area becomes 18.0.

After second nail is removed such that the area is less than the previous size, the shape will be:

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@4b21844c:image4.png

The area becomes 0.0.

(0, -6) and (0, 4) is the only order in which the nails can be removed to make the area of enclosure zero, after adhering to the rules. Since one is allowed to remove 2 nails in one turn, winning is possible. Hence the output is as depicted in the Output section of the example.

Example 2

Input

4

0 -6

4 0

0 6

-4 0

1

Output

0 -6

-4 0

NO

Explanation

Consider the following diagram:

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@4b21844c:image5.png

The above is the shape made when the given coordinates are plotted.

Now it is easy to see that removing any nail will result in the same area, therefore you choose the one which is bottom-most. So, we choose (0, -6). The shape will look as below:

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@4b21844c:image6.png

Now again removing any of the nails will lead to the same area that is zero so the one which is bottom-most and left-most, is removed.

Then the final shape will be:

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@4b21844c:image7.png

Now as the area is zero the game is over. Since a win is achieved by removing 2 nails which is maximum permissible in a player's turn, output is as depicted in the Output section in this example.

'''