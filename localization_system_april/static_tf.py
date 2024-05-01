import rclpy
import yaml
from rclpy.node import Node
import os


class PoseBroadcaster(Node):
    def __init__(self):
        super().__init__("pose_broadcaster")

        self.declare_parameter("reference_frame_id", "odom")
        self.reference_frame_id_ = self.get_parameter("reference_frame_id").value

        self.declare_parameter("child_frame_id", "tag")
        self.child_frame_id_ = self.get_parameter("child_frame_id").value

        param_path = os.path.join(
            os.getcwd(),  
            'install', 'localization_system_april', 'share', 'localization_system_april', 'tag_pose.yaml'
        )

        with open(param_path, 'r') as f:
            params = yaml.safe_load(f)

        self.print_poses(params['tag_pose'])
    
    def print_poses(self, data_poses):
        for key, value in data_poses.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    self.get_logger().info(f"{sub_key}: {sub_value}")

def main(args=None):
    rclpy.init(args=args)
    pose_broadcaster = PoseBroadcaster()
    rclpy.spin(pose_broadcaster)
    pose_broadcaster.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
