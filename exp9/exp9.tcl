# Experiment 9: Distance Vector Routing using NS2

set ns [new Simulator]

# Create trace files
set tr [open exp9.tr w]
$ns trace-all $tr

set nf [open exp9.nam w]
$ns namtrace-all $nf

# Finish procedure
proc finish {} {
    global ns tr nf
    $ns flush-trace
    close $tr
    close $nf
    exec nam exp9.nam &
    exit 0
}

# Enable Distance Vector routing
$ns rtproto DV

# Create 8 nodes
for {set i 0} {$i < 8} {incr i} {
    set n($i) [$ns node]
}

# Create network links
for {set i 0} {$i < 7} {incr i} {
    $ns duplex-link $n($i) $n([expr $i+1]) 1Mb 10ms DropTail
}

# Complete the ring topology
$ns duplex-link $n(7) $n(0) 1Mb 10ms DropTail

# Configure link layout
$ns duplex-link-op $n(0) $n(1) orient right
$ns duplex-link-op $n(1) $n(2) orient right
$ns duplex-link-op $n(2) $n(3) orient right
$ns duplex-link-op $n(3) $n(4) orient down
$ns duplex-link-op $n(4) $n(5) orient left
$ns duplex-link-op $n(5) $n(6) orient left
$ns duplex-link-op $n(6) $n(7) orient left
$ns duplex-link-op $n(7) $n(0) orient up

# Create UDP agent
set udp0 [new Agent/UDP]
$ns attach-agent $n(0) $udp0

# Create CBR traffic
set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set interval_ 0.005
$cbr0 attach-agent $udp0

# Create destination agent
set null0 [new Agent/Null]
$ns attach-agent $n(4) $null0
$ns connect $udp0 $null0

# Label source and destination
$ns at 0.0 "$n(0) label Source"
$ns at 0.0 "$n(4) label Destination"

# Start and stop traffic
$ns at 0.5 "$cbr0 start"

# Simulate a link failure and recovery
$ns rtmodel-at 1.0 down $n(3) $n(4)
$ns rtmodel-at 2.0 up $n(3) $n(4)

$ns at 4.5 "$cbr0 stop"
$ns at 5.0 "finish"

# Run simulation
$ns run
