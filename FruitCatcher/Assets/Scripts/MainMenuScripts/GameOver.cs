using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class GameOver : MonoBehaviour
{
    public static int totalScore;
    [SerializeField] TextMeshProUGUI score_text;
    // Update is called once per frame
    void Start()
    {
        score_text.text = totalScore.ToString();
    }
}
