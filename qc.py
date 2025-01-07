# Import Qiskit
from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to put the qubit into a superposition state
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Use the Aer simulator to simulate the quantum circuit
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit
job = execute(qc, simulator, shots=1024)

# Get the results
result = job.result()
counts = result.get_counts(qc)

# Print the results
print("Measurement results:", counts)

# Draw the quantum circuit
print("\nQuantum Circuit:")
print(qc.draw())
