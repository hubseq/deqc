import json
MODULE = 'deqc'

mi_template_json = {'module_version': '00.00.00', 'program_name': 'deqc', 'program_subname': '', 'program_version': '0.11.5', 'compute': {'environment': 'aws', 'language': 'Python', 'language_version': '3.7', 'vcpus': 2, 'memory': 6000}, 'program_arguments': '', 'program_input': [{'input_type': 'file', 'input_file_type': 'TXT', 'input_position': -1, 'input_prefix': '-i'}, {'input_type': 'file', 'input_file_type': 'CSV', 'input_position': -1, 'input_prefix': '-i'}, {'input_type': 'file', 'input_file_type': 'TAB', 'input_position': -1, 'input_prefix': '-i'}], 'program_output': [{'output_type': 'folder', 'output_file_type': '', 'output_position': 0, 'output_prefix': '-o'}], 'alternate_inputs': [], 'alternate_outputs': [], 'defaults': {"output_file": ""}}
with open(MODULE+'.template.json','w') as fout:
    json.dump(mi_template_json, fout)

io_dryrun_json = {'input': ['s3://hubseq-data/test/rnaseq/run_test1/deseq2/deseq2.group1-vs-group2-results.csv'], 'output': ['s3://hubseq-data/test/rnaseq/run_test1/deqc/'],  'alternate_inputs': [], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test', 'dryrun': ''}
io_json = {'input': ['s3://hubseq-data/test/rnaseq/run_test1/deseq2/deseq2.group1-vs-group2-results.csv'], 'output': ['s3://hubseq-data/test/rnaseq/run_test1/deqc/'],  'alternate_inputs': [], 'alternate_outputs': [], 'program_arguments': '-pvaluecolumn pvalue', 'sample_id': MODULE+'_test'}

with open(MODULE+'.dryrun_test.io.json','w') as fout:
    json.dump(io_dryrun_json, fout)
with open(MODULE+'.test.io.json','w') as fout:
    json.dump(io_json, fout)

# job info test JSONs                                                                                                        
job_json = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://hubseq-data/modules/"+MODULE+"/job/"+MODULE+".test.job.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
with open(MODULE+'.test.job.json','w') as fout:
    json.dump(io_json, fout)
