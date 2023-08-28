import os



# 원본 이미지
def rename_origin():
    origin_path = 'C:/Users/KimJunha/Desktop/work/synthetic data/vision nerf/input/origin_input'
    
    origin_file_names = os.listdir(origin_path)

    idx = 1

    for file_name in origin_file_names:
        new_name = "sample{0:06d}.png".format(idx)

        os.rename(os.path.join(origin_path, file_name), os.path.join(origin_path, new_name))

        idx = idx + 1



# preprocessed image
def rename_preprocessed():
    preproc_path = 'C:/Users/KimJunha/Desktop/work/synthetic data/vision nerf/input/preproc_input'

    preproc_file_names = os.listdir(preproc_path)

    idx = 1

    for file_name in preproc_file_names:
        new_name = "sample{0:06d}_normalize.png".format(idx)

        os.rename(os.path.join(preproc_path, file_name), os.path.join(preproc_path, new_name))

        idx = idx + 1

if __name__=='__main__':
    rename_origin()
    rename_preprocessed()