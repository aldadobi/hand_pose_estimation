# Hand Pose Estimation
Hand Pose Estimation project : InterHand 2.6M, FreiHAND 등의 다양한 Dataset을 기반으로 한 여러 가지의 모델에서 edge case를 해결하는 방향으로 진행중입니다.


### ACR: Attention Collaboration-based Regressor for Arbitrary Two-Hand Reconstruction. 
[ACR](https://github.com/ZhengdiYu/Arbitrary-Hands-3D-Reconstruction) : 2023 CVPR 논문으로 hand image에 대해서 mesh 정보를 inference합니다.
github에 webcam demo 및 video, image demo가 업로드되어 있으며 demos_outputs 폴더로 output이 저장됩니다.

가상환경

    conda activate ACR

#### Demo

    # Run a real-time demo:
    python -m acr.main --demo_mode webcam -t

    # Run on a single image:
    python -m acr.main --demo_mode image --inputs <PATH_TO_IMAGE>

    # Run on a folder of images:
    python -m acr.main --demo_mode folder -t --inputs <PATH_TO_FOLDER> 
    
    # Run on a video:
    python -m acr.main --demo_mode video -t --inputs <PATH_TO_VIDEO> 


---
### InterWild
[InterWild](https://github.com/facebookresearch/InterWild) : 2023 CVPR 논문으로 hand image에 대해서 bbox, 2d skeleton, mesh 정보를 infernece합니다.
github에 image folder에 대해서만 demo가 올라와 있어 webcam.py 을 실행하여 webcam demo를 사용할 수 있습니다.

가상환경

    conda activate InterWild

#### webcam demo
다음과 같은 코드로 실행되며 line 87에 webcam의 상태에 따라 숫자를 바꿔서 넣어주시면 됩니다.

    python webcam.py --gpu=0

#### image demo
를 실행하는 과정이며 /demo/images 에 원하는 image를 넣고 시각적인 output은 /demo/renders 디렉토리에 저장됩니다.

    python demo.py --gpu=0

#### save to video

이 과정에서 결과값으로 /demo/renders 디렉토리에 bbox, 2d skeleton, mesh images가 생성되며 다음과 같은 코드로 video를 만들 수 있습니다.
실행결과는 현재 디렉토리에 저장됩니다.

    python savevideocategory.py


---

### mmpose
[mmpose](https://mmpose.readthedocs.io/en/latest/demos.html) : 2d skeleton 정보를 inference합니다.
홈페이지에 image, video, webcam demo가 올라와 있습니다. 

가상환경

    conda activate openmmlab

./mmpose 에서 mmpose.py 폴더에 있는 주석처리된 코드를 실행하시면 됩니다. ./mmpose/vis_results 폴더에 결과가 저장됩니다.

---
### Dataset
Dataset은 날짜 별로 카테고리화되어 있으며 ./hand_pose/dataset/ 디렉토리에 위치하고 있습니다.
Inference 결과는 ./hand_pose/dataset/Inference/ 디렉토리에 위치하며 png 와 video로 구분되어 있습니다.


    hand_pose/
    │  
    ├─ dataset/
    │   ├─ Inference/
    │   │   ├─ ACR/
    │   │   ├─ InterWild/
    │   │   └─ mmpose/
    │   ├─ nyu_hand_dataset_v2/
    │   ├─ realsense_viewer/
    │   └─ video/

  


---
### Intel realsense Viewer
다음과 같이 코드를 입력 시 Intel RealSense Viewer가 실행되며 저장 시 .bag 파일로 저장됩니다.
가상환경은 base에서 실행하시면 됩니다.

    realsense-viewer

[rs-convert tool](https://github.com/IntelRealSense/librealsense/tree/master/tools/convert) 다음 홈페이지를 참조하여 .bag 파일을 PNG로 변환할 수 있습니다.

####예시 코드

    rs-convert -i bag/fil/path/some.bag -p output/path/some_file_prefix



