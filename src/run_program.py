import os, subprocess, sys
sys.path.append('/global_utils/src/')
# sys.path.append('global_utils/src/')
import module_utils
import deqc
        
def run_program( arg_list ):
    """
    Parameters:
    -i <input_de_files> - can take a list of files
    -type <input_de_file_type> - default deseq2
    -name <analysis_name> - default de
    -o <output_dir>
    -idtype <gene_id_type> - default ensembl
    -idcolumn <gene_column> - default gene_id
    -foldchange <minimum_foldchange> - default 2
    -pvalue <pvalue_cutoff> - default 0.05
    -pvaluecolumn <pvalue_column> - default padj
    """
    print('ARG LIST: {}'.format(str(arg_list)))
    input_args = module_utils.getArgument( arg_list, '-i', 'list' )
    output_dir = module_utils.getArgument( arg_list, '-o' )
    de_file_type = module_utils.getArgument( arg_list, '-type', 'implicit', 'deseq2' )
    de_name = module_utils.getArgument( arg_list, '-name', 'implicit', 'de' )
    id_type = module_utils.getArgument( arg_list, '-idtype', 'implicit', 'ensembl' )
    id_column = module_utils.getArgument( arg_list, '-idcolumn', 'implicit', 'gene_id' )
    fold_change = float(module_utils.getArgument( arg_list, '-foldchange', 'implicit', 2 ))
    pvalue = float(module_utils.getArgument( arg_list, '-pvalue', 'implicit', 0.05 ))
    pvalue_column = module_utils.getArgument( arg_list, '-pvaluecolumn', 'implicit', 'padj' )
    if output_dir not in [[], '']:
        os.chdir( output_dir )
    if input_args != []:
        # create input JSON
        input_json = {'analysis_name': de_name, 'input_file': input_args, 'input_file_type': de_file_type, \
                      'output_dir': output_dir, 'gene_id_type': id_type, 'gene_id_column': id_column, \
                      'fold_change_cutoff': fold_change, 'pvalue_cutoff': pvalue, 'pvalue_column': pvalue_column}        
        # run DE QC
        deqc.deqc( input_json )
    return

if __name__ == '__main__':
    print('in run_program.py')
    run_program( sys.argv[1:] )
