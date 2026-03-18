/// A robust PID controller implementation for safety-critical systems.
/// Avoids panic-inducing patterns and ensures deterministic execution.

pub struct PidController {
    pub kp: f64,
    pub ki: f64,
    pub kd: f64,
    pub setpoint: f64,
    dt: f64,
    integral: f64,
    prev_error: f64,
}

impl PidController {
    pub fn new(kp: f64, ki: f64, kd: f64, setpoint: f64, dt: f64) -> Self {
        Self {
            kp,
            ki,
            kd,
            setpoint,
            dt,
            integral: 0.0,
            prev_error: 0.0,
        }
    }

    /// Computes the control signal. Returns a Result to handle potential 
    /// numerical instabilities if dt were zero or invalid.
    pub fn compute(&mut self, current_velocity: f64) -> Result<f64, String> {
        if self.dt <= 0.0 {
            return Err("Time step (dt) must be positive to ensure stability.".to_string());
        }

        let error = self.setpoint - current_velocity;
        
        // Anti-windup logic could be added here for Ki
        self.integral += error * self.dt;
        
        let derivative = (error - self.prev_error) / self.dt;
        let control_output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative);
        
        self.prev_error = error;

        Ok(control_output)
    }
}

fn main() {
    let mut controller = PidController::new(2.0, 0.5, 0.1, 10.0, 0.1);
    let mut current_velocity = 0.0;

    for _ in 0..100 {
        match controller.compute(current_velocity) {
            Ok(output) => {
                // Simple first-order motor model: v = v + a*dt
                current_velocity += output * 0.1;
                println!("Current Velocity: {:.2}", current_velocity);
            }
            Err(e) => {
                eprintln!("Controller Error: {}", e);
                break;
            }
        }
    }
}