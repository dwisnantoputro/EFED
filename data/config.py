# config.py

cfg = {
    'name': 'FaceCPU',
    'feature_maps': [[32, 32], [16, 16], [8, 8]],
    'min_dim': 1024,
    'steps': [32, 64, 128],
    'min_sizes': [[32, 64, 96, 128], [192, 256], [384, 512]],
    'aspect_ratios': [[1], [1], [1]],
    'variance': [0.1, 0.2],
    'clip': False,
    'loc_weight': 2.0,
    'conf_weight': 1.0,
    'gpu_train': True
}
