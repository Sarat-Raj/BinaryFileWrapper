

module arbiter_puf (
    input wire [N-1:0] challenge, // N-bit challenge input
    output reg [M-1:0] response // M-bit response output
);
    parameter N = 4; // Number of challenge bits
    parameter M = 1; // Number of response bits
    parameter DELAY = 16'hFFFF; // 4xN-bit delay values for muxes

    wire [N-1:0] mux_inputs [M-1:0];
    wire [M-1:0] mux_outputs;
    
    // Instantiate mux modules with challenge bits and DELAY parameter
    genvar i, j;
    generate
        for (i = 0; i < M; i = i + 1) begin : GEN_MUX
            generate
                for (j = 0; j < N; j = j + 1) begin : GEN_CHALLENGE_MUX
                    mux #(DELAY[(4*(i*N + j) + 3): (4*(i*N + j))], 2'b01) 
                        MUX (
                            .sel(challenge[j]),
                            .a(1'b0),
                            .b(1'b1),
                            .out(mux_inputs[i][j])
                        );
                end
            endgenerate
            
            // Arbiter logic to generate response bits
            always @* begin
                int k;
                response[i] = 1'b1;
                for (k = 0; k < N; k = k + 1) begin
                    if (!mux_inputs[i][k]) begin
                        response[i] = 1'b0;
                        break;
                    end
                end
            end
        end
    endgenerate
endmodule
