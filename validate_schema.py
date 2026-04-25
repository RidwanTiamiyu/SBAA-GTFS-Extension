import csv
import sys

# Define Federal Compliance Thresholds
# Standard: 8.33% maximum grade for ADA accessible routes
ADA_MAX_SLOPE = 8.33

def run_compliance_audit(file_path):
    print(f"--- SBAA FISCAL GUARDRAIL: STARTING AUDIT FOR {file_path} ---")
    
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            passed_nodes = 0
            failed_nodes = 0
            
            for row in reader:
                stop_id = row['stop_id']
                slope = float(row['slope_gradient'])
                
                # Logic: Flag utilization risk if slope exceeds federal mandate
                if slope > ADA_MAX_SLOPE:
                    print(f"[!] WARNING: {stop_id} FAILS compliance. Slope: {slope}% (Max: {ADA_MAX_SLOPE}%)")
                    failed_nodes += 1
                else:
                    passed_nodes += 1
            
            print(f"--- AUDIT COMPLETE ---")
            print(f"Nodes Compliant: {passed_nodes}")
            print(f"Nodes Non-Compliant (Utilization Risk): {failed_nodes}")
            
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please ensure data file is in root directory.")

if __name__ == "__main__":
    # Defaulting to the SBAA standard behavioral constraints file
    target_data = 'behavioral_constraints.txt'
    run_compliance_audit(target_data)
