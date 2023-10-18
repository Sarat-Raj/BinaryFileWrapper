// tb_arbiter_puf.v

module tb_arbiter_puf();

    // Parameters
    parameter N = 4; // Number of challenge bits
    parameter M = 1; // Number of response bits
    parameter DELAY = 16'hFFFF; // Delay parameter (4xN-bit delay values for muxes)

    // Signals
    reg [N-1:0] challenge;
    wire [M-1:0] response;

    // Instantiate arbiter_puf module
    arbiter_puf #(.N(N), .M(M), .DELAY(DELAY)) uut (
        .challenge(challenge),
        .response(response)
    );

    // Clock and Reset
    reg clk;
    reg rst;

    // Testbench code here

    // Stimulus
    initial begin
        clk = 0;
        rst = 1;
        challenge = 4'b0000; // Set initial challenge value

        // Apply reset
        #10 rst = 0;

        // Toggle clock and apply stimulus
        forever #5 clk = ~clk;
    end

    // Monitor
    always @(posedge clk) begin
        // Display challenge and response on each positive clock edge
        $display("Challenge: %b, Response: %b", challenge, response);
        // Add any additional checks/assertions based on your test cases
        // Example: assert(response == expected_response);
    end

endmodule
