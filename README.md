# UAV-Assisted 5G Networks - Application by Quantum Walk

[![Build Status](https://github.com/willnien10005914/skw-element-distinctness/blob/main/coverage.png)](https://github.com/willnien10005914/skw-element-distinctness/blob/main/coverage.png)

[![Build Status](https://github.com/willnien10005914/skw-element-distinctness/blob/main/uav.png)](https://github.com/willnien10005914/skw-element-distinctness/blob/main/uav.png)

### 5G Network Coverage MAP - Bad
[![Build Status](https://github.com/willnien10005914/skw-element-distinctness/blob/main/bad_coverage_1.png)](https://github.com/willnien10005914/skw-element-distinctness/blob/main/bad_coverage_1.png)

### Quantum Walk 
[![Build Status](https://github.com/willnien10005914/uav-network-quantum-walk/blob/main/quantum_circuit.png)](https://github.com/willnien10005914/uav-network-quantum-walk/blob/main/quantum_circuit.png)

### 5G Network Coverage MAP - Good
[![Build Status](https://github.com/willnien10005914/skw-element-distinctness/blob/main/good_coverage_1.png)](https://github.com/willnien10005914/skw-element-distinctness/blob/main/good_coverage_1.png)

## Installation
1. Please install related python packages : pip install -r requirements.txt
2. Install PX4 : make px4_sitl jmavsim
3. Install QGroundControl

## Description
The idea pertains to the context of Enhanced Mobile Broadband (eMBB) scenarios, aiming to achieve extensive coverage using drones (UAVs). This involves ensuring minimal drone duplication within the same area to maximize coverage.

This application determines the optimal drone flight locations using either the element distinctness or triangle-finding algorithm, we can proceed to initiate the takeoff command.
