using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Ball : MonoBehaviour
{
    [SerializeField]
    private float ball_velocity = 20f, ball_speed_multiplier = 0.05f;
    private float ball_velocity_y, ball_velocity_x;
    private Rigidbody ball_rb;
    private Transform Player1, Player2;
    private Vector3 default_position;

    private GameObject GameController;

    private bool started = false;

    // Start is called before the first frame update
    void Start()
    {
        Player1 = GameObject.Find("Player1").GetComponent<Transform>();
        Player2 = GameObject.Find("Player2").GetComponent<Transform>();

        GameController = GameObject.Find("GameController");


        ball_rb = this.GetComponent<Rigidbody>();
        default_position = ball_rb.transform.position;
        ball_velocity_x = ball_velocity;
        ball_velocity_y = ball_velocity;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
            started = true;
        if(ball_rb.gameObject.transform.position.x > Player2.position.x || ball_rb.gameObject.transform.position.x < Player1.position.x)
        {
            if (ball_rb.gameObject.transform.position.x > Player2.position.x)
                GameController.GetComponent<GameController>().p1_pont += 1;
            else
                GameController.GetComponent<GameController>().p2_pont += 1;
            ball_velocity_x = ball_velocity * ball_rb.velocity.normalized.x;
            ball_velocity_y = ball_velocity * ball_rb.velocity.normalized.z;
            ball_rb.gameObject.transform.position = default_position;
            ball_rb.velocity *= 0;
            started = false;
        }

        if(started)
            ball_rb.velocity = ((Vector3.right * ball_velocity_x) + (Vector3.forward * ball_velocity_y)) * 30 * Time.deltaTime;
    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.name == "Up" || collision.gameObject.name == "Down")
            ball_velocity_y *= -1;

        if (collision.gameObject.name == "Player1" || collision.gameObject.name == "Player2")
        {
            ball_velocity_x *= -1;
            ball_velocity_y += ball_velocity_y * ball_speed_multiplier;
            ball_velocity_x += ball_velocity_x * ball_speed_multiplier + 0.02f;
        } 
    }
}
