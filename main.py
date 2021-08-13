from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
 
def fn_start_document_summarize():
    print("記事を入力してください。")
    contents = str(input())    
    document = ''.join(contents)
    
    
    auto_abstractor = AutoAbstractor()
    auto_abstractor.tokenizable_doc = MeCabTokenizer()
    auto_abstractor.delimiter_list = ["。", "\n"]
    abstractable_doc = TopNRankAbstractor()
    result = auto_abstractor.summarize(document, abstractable_doc)
 
    print('-------------要約結果-------------')
    # Output result.
    for sentence in result["summarize_result"]:
        print(sentence)
    print("---------------------------------")
    
if __name__ == '__main__':
    fn_start_document_summarize()