#include <iostream>
#include<sstream>
#include<unordered_map>
#include<string>
#include<vector>

using namespace std;

int main(){
    int count;
    cout<<"Enter number of scentence:";
    cin >> count;
    cin.ignore();

    vector<string> corpus(count);
    cout<<"Enter the scentence";
    for(int i=0;i<count;++i){
        cout<<"Scentence"<<i+1<<":";
        getline(cin,corpus[i]);
        corpus[i] = "<s> " + corpus[i] + " </s>";
    }

    cout<<"Enter test scentence:";
    string test;
    getline(cin,test);
    test= "<s> " + test + " </s>";

    vector<string> test_words;
    stringstream ss_test(test);
    string word;
    while(ss_test >> word){
        test_words.push_back(word);
    }

    unordered_map<string,int> unigram;
    unordered_map<string, unordered_map<string,int>> bigram;

    for (const auto& scentence:corpus){
        stringstream ss(scentence);
        string prev_word = "<s>",word;
        while(ss>>word){
            unigram[word]++;
            bigram[prev_word][word]++;
            prev_word=word;
        }
    }

    cout<<"Unigram"<<endl;
    for(const auto& word:test_words){
        if(unigram.find(word)!= unigram.end()){
            cout<<word<<":"<<unigram[word]<<endl;
        }
    }

    cout<<"Bigram"<<endl;
    for(size_t i=0;i<test_words.size()-1;++i){
        if(bigram[test_words[i]].find(test_words[i+1])!= bigram[test_words[i]].end()){
            cout<<"("<<test_words[i]<<","<<test_words[i+1]<<")"<<bigram[test_words[i]][test_words[i+1]]<<endl;
        }
    }

    float probability = 1.0;
    for(size_t i=0;i<test_words.size()-1;++i){
         if(bigram[test_words[i]].find(test_words[i+1])!= bigram[test_words[i]].end()){
            probability *= static_cast<float>(bigram[test_words[i]][test_words[i+1]])/unigram[test_words[i]];
         }else{
            break;
         }
    }
    cout << "Probability: "<<probability<<endl;
    return 0;
}