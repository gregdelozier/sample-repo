//varibles that store the x and y position of the ball
ball_x = 0
ball_y = 0

//stores the time (in seconds) of the ball's lifespan
time = 0

//stores the speed of the ball
dy = 0

function setup() {
    createCanvas(600, 600);
}

//function to create a ball when called
function ball(){
  circle(ball_x, ball_y, 40)
}

function draw() {
    background(200);
    
    //logs the x and y postion of the user's mouseclick
    console.log(ball_x, ball_y)

    if (ball_x > 0 && ball_y > 0) {

      //logs the time when the user clicks their mouse
      console.log(deltaTime)

      //calculates the time (seconds)
      time = (deltaTime * .001) + time

      //call function to create a ball
      ball()

      //calculate the speed of the ball
      dy = dy + ((time/10) * 10)

      //make the ball drop according gravity
      ball_y = ball_y + (dy * (time))

      //check to see when the ball hits the floor to reverse its direction
      if (ball_y >= 600){
        ball_y = 600
        dy = -dy + (time * 10)
      }  
    }
}

function mousePressed() {
    console.log("mouse pressed", mouseX, mouseY, deltaTime)
    
        //set the x and y of the mouse click eqaul to the x and y position of the ball
        ball_x = mouseX
        ball_y = mouseY
        
        //reset the time and speed of the ball
        time = 0
        dy = 0
        
}