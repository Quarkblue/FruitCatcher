using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;   
using UnityEngine.SceneManagement;  
using TMPro;
using UnityEditor;

public class ScoreManager : MonoBehaviour
{
    public TextMeshProUGUI scoreText;

    private int score;

    public GameObject hat;
    
    void Start()
    {
        
    }

    
    void Update()
    {
        
        scoreText.text = score.ToString();  
        
    }
    void OnTriggerEnter2D(Collider2D target)
    {
        if(target.tag == "Bomb")
        {
            GameOver.totalScore = score;
            SceneManager.LoadScene("GameOver");    
        }   
        
    }

    void OnTriggerExit2D(Collider2D target)
    {
        if(target.tag == "Fruit")
        {
            Destroy(target.gameObject);
            score++;
        }
        
    }
    IEnumerator WaitTillRestart()
    {
        yield return new WaitForSeconds(2f);
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }

}
