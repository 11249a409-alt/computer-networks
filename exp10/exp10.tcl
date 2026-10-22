# Experiment 10: Link State Routing Algorithm using NS2

set ns [new Simulator]

# Define colors for traffic
$ns color 1 Red
$ns color 2 Blue

# Create trace files
set tr [open exp10.tr w]
$ns trace-all $tr

set nf [open exp10.nam w]
$ns namtrace-all $nf

# Finish procedure
proc finish {} {
    global ns tr nf
    $ns flush-trace
    close $tr
    close $nf
    exec nam exp10.nam &
    exit 0
}

# Enable Link State routing
$ns rtproto LS

# Create 12 nodes
for {set i 0} {$i < 12} {incr i} {
    set n($i) [$ns node]
}

# Create links between nodes
for {set i 0} {$i < 11} {incr i} {
    $ns duplex-link $n($i) $n([expr $i+1]) 1Mb 10ms DropTail
}

# Add alternative paths
$ns duplex-link $n(0) $n(4) 1Mb 15ms DropTail
$ns duplex-link $n(3) $n(7) 1Mb 15ms DropTail
$ns duplex-link $n(6) $n(10) 1Mb 15ms DropTail
$ns duplex-link $n(0) $n(11) 1Mb 20ms DropTail

# First UDP connection: node 0 to node 8
set udp0 [new Agent/UDP]
$ns attach-agent $n(0) $udp0

set null0 [new Agent/Null]
$ns attach-agent $n(8) $null0
$ns connect $udp0 $null0
$udp0 set fid_ 1

set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 512
$cbr0 set interval_ 0.05
$cbr0 attach-agent $udp0

# Second UDP connection: node 1 to node 11
set udp1 [new Agent/UDP]
$ns attach-agent $n(1) $udp1

set null1 [new Agent/Null]
$ns attach-agent $n(11) $null1
$ns connect $udp1 $null1
$udp1 set fid_ 2

set cbr1 [new Application/Traffic/CBR]
$cbr1 set packetSize_ 512
$cbr1 set interval_ 0.05
$cbr1 attach-agent $udp1

# Label important nodes
$ns at 0.0 "$n(0) label Source1"
$ns at 0.0 "$n(8) label Destination1"
$ns at 0.0 "$n(1) label Source2"
$ns at 0.0 "$n(11) label Destination2"

# Start traffic
$ns at 1.0 "$cbr0 start"
$ns at 2.0 "$cbr1 start"

# Simulate a link failure and recovery
$ns rtmodel-at 5.0 down $n(6) $n(7)
$ns rtmodel-at 8.0 up $n(6) $n(7)

# Stop traffic and finish
$ns at 10.0 "$cbr0 stop"
$ns at 10.0 "$cbr1 stop"
$ns at 11.0 "finish"

# Run simulation
$ns run
