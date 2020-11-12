using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    GameObject Player1, Player2;
    [SerializeField]
    private float player_speed = 20f;
    // Start is called before the first frame update
    void Start()
    {
        Player1 = GameObject.Find("Player1");
        Player2 = GameObject.Find("Player2");
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(KeyCode.W))
        {
            if (Player1.transform.position.z <= 9)
                Player1.transform.position += Vector3.forward * player_speed * Time.deltaTime;
        }
        if (Input.GetKey(KeyCode.S))
        {
            if(Player1.transform.position.z >= -8.5f)
                Player1.transform.position += Vector3.back * player_speed * Time.deltaTime;
        }

        if (Input.GetKey(KeyCode.UpArrow))
        {
            if (Player2.transform.position.z <= 9)
                Player2.transform.position += Vector3.forward * player_speed * Time.deltaTime;
        }
        if (Input.GetKey(KeyCode.DownArrow))
        {
            if (Player2.transform.position.z >= -8.5f)
                Player2.transform.position += Vector3.back * player_speed * Time.deltaTime;
        }
    }
}
