using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameController : MonoBehaviour
{
    [HideInInspector]
    public int p1_pont = 0, p2_pont = 0;

    private Text p1_score, p2_score;

    private void Awake()
    {
        QualitySettings.vSyncCount = 0;
        Application.targetFrameRate = 60;
    }

    // Start is called before the first frame update
    void Start()
    {
        p1_score = GameObject.Find("Player1_pont").GetComponent<Text>();
        p2_score = GameObject.Find("Player2_pont").GetComponent<Text>();
    }

    // Update is called once per frame
    void Update()
    {
        p1_score.text = "Player 1: " + p1_pont;
        p2_score.text = "Player 2: " + p2_pont;
        if (Input.GetKeyDown(KeyCode.Escape))
            Application.Quit();
    }
}
