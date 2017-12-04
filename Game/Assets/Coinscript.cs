using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class Coinscript : MonoBehaviour {

    public Object objectName;

    // Use this for initialization
    void Start () {
        float x = Random.Range(-10.0f, 10f);
        float y = Random.Range(-5f, 5f);
        transform.position = new Vector3(x, y, -5);


    }
	
	// Update is called once per frame
	void Update () {
		
	}

    private void OnMouseDown()
    {
        GlobalControl.coins++;
        GameObject.Find("Text").GetComponent<Text>().text = "Total Score = " + GlobalControl.coins;
        float x = Random.Range(-10.0f, 10f);
        float y = Random.Range(-5f, 5f);
        transform.position = new Vector3(x, y, -5);
    }
}
