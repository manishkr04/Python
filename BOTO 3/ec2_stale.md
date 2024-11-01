## AWS Cloud Cost Optimization: Identifying Stale EBS Snapshots

--- In this example, we will develop an AWS Lambda function designed to identify and delete stale EBS snapshots that are no longer associated with any active EC2 instances, thereby reducing unnecessary storage costs.

## Description:
--- The Lambda function retrieves all EBS snapshots owned by the account (identified as 'self') and compiles a list of active EC2 instances, including both running and stopped states. For each snapshot, the function checks whether the associated volume (if it exists) is linked to any active instance. If a stale snapshot is detected—meaning its associated volume is not connected to any active instance—the function will delete the snapshot. This proactive approach ensures efficient management of EBS snapshots and optimizes cloud storage costs by eliminating unused resources.