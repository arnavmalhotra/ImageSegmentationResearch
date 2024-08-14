import nibabel as nib

# Load the NIfTI file
nii_file = 'labelsTr\case_0000.nii.gz'
img = nib.load(nii_file)
data = img.get_fdata()

# Print the shape of the data
print(f'Data shape: {data.shape}')

# Number of slices in each dimension
num_slices_axial = data.shape[2]    # Typically, the third dimension is the axial slice
num_slices_coronal = data.shape[1]  # Typically, the second dimension is the coronal slice
num_slices_sagittal = data.shape[0] # Typically, the first dimension is the sagittal slice

print(f'Number of axial slices: {num_slices_axial}')
print(f'Number of coronal slices: {num_slices_coronal}')
print(f'Number of sagittal slices: {num_slices_sagittal}')
