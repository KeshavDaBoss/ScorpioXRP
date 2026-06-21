This is Scorpio, our Experiential Robotics Platform (XRP) for the Team India Nationals Selections [The Bharatiya Yantra Khel Mahostav 2026] for the FIRST Global Challenge!
We programmed this robot within the span of about 3 weeks, taking it from just a hardware assembly kit to a working, Tank-Drive robot with a working arm and even a hardcoded autonomous mode.

# Step 1: Assembling and Learning Hardware

Assembly of the XRP Kit proved to be extermely easy. Most parts just snap into place and be plugged into the UART pins on the XRP's PCB.

Some teams planned on building a custom Chasis, but we did not do so for 2 honest reasons-
1) Our school did not wish to use too much of a Budget on this.
2) We honestly did not know what to even make the Chasis like (this decision would bite us in the back later in the competition)

# Step 2: The Scorpion's Arm

Once assembled, our next step was to start Coding the Robot as well as simultaneously.

Our Arm took about the time of a week.
The design for our arm was an edited version of a design we found on printables (https://www.printables.com/model/919002). We changed the arm to instead function with just 3 servo motors (which were the regulation limit).
Later testing showed that our printed model's gear system was not funstional, and that one arm would have to be glued in place for it to pick up the necessary items.

# Step 3: The Code

During the same week, unfortunately the code had moved nowhere. I hadn't found a way to connect the gamepad and was still exploring my options.

The first was to use WPILib on VSCode.
The second was to use the XRP IDE, a site that connected to the robot directly and offered the option to use Blockly (a 'Scratch' type of block coding) or MicroPython.

At last, we went with XRP IDE, because I found out (quite late) that the XRP IDE made gamepad connection extermely easy. It almost meant I did not have to learn the MicroPython Library, because I could do initial prototyping in Blockly and make the final, complete iteration in MicroPython.

## The Autonomous Mode

During the competition, we learnt that our hard-coded values for Autonomous mode was the second best one present, losing out only to the overall competition winner.

# Testing Testing Testing

Now that the robot was complete, during the last week we handed the control to our driver for practice and testing.

And *this* was the moment we realised there was a problem we hadn't even thought of. Weight Distribution.
Somehow placing the robot towards the front shifted the weight away from the wheels, making the traction on the ground reduce (especially on our right wheel).

Placing the arm on the back meant better traction on the ground, also giving the XRP its name.

# The Great Game and The Results

You can see the game in the Resources folder.

The competition consisted of Qualifying matches where 18 Teams would play 2 matches each, and the 8 teams with the highest average score would then go on to Head-on-Head Playoffs.

Our First match went absolutely horrible beyond any expectations. The Autonomous mode made huge errors for reasons we still don't know, and the robot stalled for 1:30 mins to 2:00 mins out of the 2:30 min match.
In the end, managed to somehow score 65 points.

Our Second match was miles better, with almost zero stalling, and a decent score 190.

Unfortunately, given the performance in Match 1, we only managed placing 9th, losing out by just 8 points.

# Lessons

What we should be doing different next time—

1) Use a custom, more lightweight chassis
2) Forklift kind of arm might work better
3) Make sure practice arena is 100% accurate
4) Replace Castor wheels
5) Give our driver tons and tons of practice
6) Find a way to add emergency stop to autonomous mode by changing XRPLib code or any other way# ScorpioXRP
