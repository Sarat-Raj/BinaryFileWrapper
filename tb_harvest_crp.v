

module tb_harvest_crp;

    // Parameters
    parameter N_CHALLENGE = 4; // Number of challenge bits
    parameter N_RESPONSE = 32; // Number of response bits
    parameter NUM_CONFIGURATIONS = 16; // Number of PUF configurations

    // Signals
    reg [N_CHALLENGE-1:0] challenge;
    reg [N_RESPONSE-1:0] responses [NUM_CONFIGURATIONS-1:0];

    // Clock and Reset
    reg clk;
    reg rst;

    // Instantiate arbiter_puf module for different configurations
    genvar i;
    generate
        for (i = 0; i < NUM_CONFIGURATIONS; i = i + 1) begin : GEN_PUF_CONFIG
            arbiter_puf #(.N(N_CHALLENGE), .M(N_RESPONSE), .DELAY(DELAY[i])) uut (
                .challenge(challenge),
                .response(responses[i])
            );
        end
    endgenerate

    // Testbench code here

    // Stimulus
    initial begin
        clk = 0;
        rst = 1;
        challenge = 4'b0000; // Initial challenge value
        
        // Apply reset
        #10 rst = 0;

        // Generate CRPs for all configurations
        for (i = 0; i < NUM_CONFIGURATIONS; i = i + 1) begin
            // Set challenge value
            challenge = i;
            
            // Wait for a few clock cycles (adjust based on your design)
            #10;
            
            // Display CRP
            $display("Challenge: %b, Response: %b", challenge, responses[i]);
        end
        
        // End simulation
        #10 $finish;
    end

    // Clock generation
    always #5 clk = ~clk;

    // Include delay configurations generated by delay.py
    parameter [3:0] DELAY [15:0] = {16'hXXXX, 16'hYYYY, /* ... */ };

endmodule
