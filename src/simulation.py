import mujoco_py
import os

def main():
    path = "/home/aortz99/SA_PPO/src/"
    appended_path = os.path.join(path,"sarsa_humanoid_sgld.model")
    mujoco_py.load_model_from_path(appended_path)
    print(appended_path)
    mujoco_py.MjSim(open(appended_path))

if __name__ == "__main__":
    main()