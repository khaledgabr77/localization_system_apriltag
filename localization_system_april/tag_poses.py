import yaml
import os

class PoseBroadcaster():
    def __init__(self):
        super().__init__()

        param_path = os.path.join(
            os.getcwd(),
            'install', 'localization_system_april', 'share', 'localization_system_april', 'tag_pose.yaml'
        )

        with open(param_path, 'r') as f:
            self.params = yaml.safe_load(f)
        
        self.tag_poses = {}


    def get_pose_data(self):
        for index, pose_data in self.params['tag_poses'].items():
            self.tag_poses[int(index)] = [
                pose_data[0],
                pose_data[1],
                pose_data[2],
                pose_data[3],
                pose_data[4],
                pose_data[5]
    ]
        return self.tag_poses

def main(args=None):
    pose_broadcaster = PoseBroadcaster()
    pose_data = pose_broadcaster.get_pose_data()
    print(pose_data)

if __name__ == '__main__':
    main()
