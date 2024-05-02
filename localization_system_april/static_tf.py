import rclpy
import yaml
import os
from rclpy.node import Node
from geometry_msgs.msg import PoseArray, Pose
import tf2_ros
from tf2_ros import Buffer, TransformListener
from .tag_poses import PoseBroadcaster
from transformations import quaternion_from_euler

class StaticTFPublisher(Node):
    def __init__(self):
        super().__init__("static_tf_publisher")

        self.tf_buffer_ = Buffer()
        self.tf_listener_ = TransformListener(self.tf_buffer_, self)

        self.timer = self.create_timer(0.1, self.tag_callback)

        self.publisher_ = self.create_publisher(
            PoseArray,
            'static_tf_tag',
            10)

        # param_path = os.path.join(
        #     os.getcwd(),
        #     'install', 'localization_system_april', 'share', 'localization_system_april', 'tag_pose.yaml'
        # )

        # with open(param_path, 'r') as f:
        #     params = yaml.safe_load(f)
        # self.get_logger().info(f'PARAM Pose {params}')
    def tag_callback(self):
        pose_array_msg = PoseArray()

        try:
            pose_broadcaster = PoseBroadcaster()
            pose_values = pose_broadcaster.get_pose_data()
            
            for tag_id, pose_data in pose_values.items():
                # print(f"Tag ID: {tag_id}, Pose Data: {pose_data}")
                if pose_data is not None:
                    
                    print(f"Tag ID: {tag_id}, Pose Data: {pose_data}")
                      # Convert set to list
                    pose_msg = Pose()
                    pose_msg.position.x = float(pose_data[0])
                    pose_msg.position.y = float(pose_data[1])
                    pose_msg.position.z = float(pose_data[2])
                    #print(f"Pose_x: {pose_msg.position.x}, Pose_y: {pose_msg.position.y}, Pose_z: {pose_msg.position.z}")

                    q = quaternion_from_euler(pose_data[3], pose_data[4], pose_data[5])
                    pose_msg.orientation.x = q[0]
                    pose_msg.orientation.y = q[1]
                    pose_msg.orientation.z = q[2]
                    pose_msg.orientation.w = q[3]
                                
                    pose_array_msg.poses.append(pose_msg)

                    self.publisher_.publish(pose_array_msg)
            else:
                self.get_logger().warn("Pose values are None.")

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            self.get_logger().warn(f"Exception occurred: {e}")
        # tag_poses = params['tag_pose']
        # self.get_logger().info(f'Tag Pose {tag_poses}')

        # pose_array_msg = PoseArray()
        # pose_array_msg.header.frame_id = self.reference_frame_id_

        # br = tf2_ros.TransformBroadcaster(self)
        # for tag_id, pose_data in tag_poses.items():
        #     t = geometry_msgs.msg.TransformStamped()
        #     t.header.stamp = self.get_clock().now().to_msg()
        #     t.header.frame_id = "map"
        #     t.child_frame_id = "tag" + "_" + str(tag_id)
        #     self.get_logger().info(f'Referance_frame: {t.header.frame_id} : Child_Frame: {t.child_frame_id}')

        #     t.transform.translation.x = float(pose_data[0])
        #     t.transform.translation.y = float(pose_data[1])
        #     t.transform.translation.z = float(pose_data[2])
            
        #     q = quaternion_from_euler(pose_data[3], pose_data[4], pose_data[5])
        #     t.transform.rotation.x = q[0]
        #     t.transform.rotation.y = q[1]
        #     t.transform.rotation.z = q[2]
        #     t.transform.rotation.w = q[3]

        #     br.sendTransform(t)

        #     # Add the pose to the PoseArray
        #     pose = Pose()
        #     pose.position.x = t.transform.translation.x
        #     pose.position.y = t.transform.translation.y
        #     pose.position.z = t.transform.translation.z
        #     pose.orientation.x = q[0]
        #     pose.orientation.y = q[1]
        #     pose.orientation.z = q[2]
        #     pose.orientation.w = q[3]
        #     pose_array_msg.poses.append(pose)

        # # self.get_logger().info(f'Tag Pose {pose_array_msg}')
        # # Publish the PoseArray
        # self.publisher_.publish(pose_array_msg)
    
def main(args=None):
    rclpy.init(args=args)
    static_tf_publisher = StaticTFPublisher()
    rclpy.spin(static_tf_publisher)
    static_tf_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
