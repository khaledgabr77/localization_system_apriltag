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
            os.getcwd(),  # Get current working directory
            'install', 'localization_system_april', 'share', 'localization_system_april', 'tag_pose.yaml'
        )

        # self.get_logger().info("Parameter file path: %s", param_path)


        with open(param_path, 'r') as f:
            params = yaml.safe_load(f)
        
        print(params)
        tag_info = params.get('tag_pose', {})
        
        # # self.get_logger().info("HI")
        # for tag_id, pose_value in tag_info.items():
        #     pose_info = [float(value) for value in pose_value]
        #     # self.get_logger().info(f'Tag Pose {tag_id}: {pose_info}')
        #     print(f'Tag Pose {tag_id}: {pose_info}')
        # # self.get_logger().info("BYE")


def main(args=None):
    rclpy.init(args=args)
    pose_broadcaster = PoseBroadcaster()
    rclpy.spin(pose_broadcaster)
    pose_broadcaster.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
