//user editable variables, affect ball
var cx = 2, //starting x, default is 0
    cy = 200, //starting y, default is 200
    velocity = 5, // velocity at specified angle
    angle = 0, // ----> is 0

//user editable variables, affect world
    radius = 10, //default is 10
    gravity = 0.2, //default is 0.2
    damping = 0.9, //default is 0.9
    friction = 0.8; //default is 0.8

    let drawPath = false;


//don't edit these
let frame = 20;
let circles = [];

function setup() {
  //just to make things easier, I'm working with degrees
  angleMode(DEGREES);

  //splitting user inputted velocity into horizontal and vertical components
  vx = velocity * cos(angle);
  vy = -velocity * sin(angle);
  
  createCanvas(500, 400);
}

function draw() {
  //pretty standard frame rate
  frameRate(100);
  background("grey");

  
  //this function call handles all of the physics
  circlephysics();
  
  if(drawPath){
    circles.forEach(circ => {
      circle(circ.x, circ.y, 5);
    })
    
  }
  
}

function circlephysics() {
  frame++;
  if (frame%7 == 0) {
    circles.push(
      {x: cx, y: cy}
    );
  }
  
  if (cx + radius >= canvas.width) { //condition: crossing right side
    vx = -vx * damping;
    cx = canvas.width - radius;
    pathTrail = false;
    
  } else if (cx - radius <= 0) { //condition: crossing left side
    vx = -vx * damping;
    cx = radius;
    pathTrail = false;
  }
  if (cy + radius >= canvas.height) { //condition: touching bottom
    vy = -vy * damping;
    cy = canvas.height - radius;
    
    //ensures ball rolls to a smooth stop
    vx *= friction;
    pathTrail = false;
    
  } else if (cy - radius <= 0) { //condition: touching top
    vy = -vy * damping;
    cy = radius;
    pathTrail = false;
  }

  //constant gravitational force
  vy += gravity; 

  //updating ball position
  cx += vx;
  cy += vy;
  
  
  //drawing circle
  circle(cx, cy, radius);
  
  
  
}


function mousePressed() { //stops ball from moving and sets position to cursor
  cx = mouseX;
  cy = mouseY;

  vx = 0;
  vy = 0;
}



function mouseDragged() { //deviation from mouse cursor is new velocity
  vx = (mouseX - cx) * 0.3;
  vy = (mouseY - cy) * 0.3;

  circlephysics();
}
