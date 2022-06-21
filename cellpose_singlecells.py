





python -m cellpose --dir /hpc/projects/gpfs_ML/ML_group/JRB/segmentation/Cellpose_testing/testdata2_large/ --pretrained_model cyto --diameter 150 --chan 2 --chan2 3 --flow_threshold 0.4 --use_gpu --save_tif --verbose


# Has issue with large files--need to use pickle protocol = 4.0 or higher. Haven't explored this yet. 