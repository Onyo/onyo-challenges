//
//  RestaurantViewController.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/13/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit

class RestaurantViewController: UIViewController {

    // MARK: - Properties
    
    @IBOutlet var tableView: UITableView!
    
    var companies = [Company]()
    
    // MARK: - Life Cycle
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        configContent()
        fetchCompanyList()
    }
    
    // MARK: - Configuration
    
    func configContent() {
        tableView.rowHeight = UITableViewAutomaticDimension
        tableView.estimatedRowHeight = 220.0
    }
    
    // MARK: - API handlers
    
    func fetchCompanyList() {
        OnyoAPIManager.sharedInstance.fetchCompanyList({ (companies) in
            self.companies = companies
            self.tableView.reloadData()
        }) { (error) in
            
        }
    }
    
}

extension RestaurantViewController: UITableViewDataSource {
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return companies.count
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cellIdentifier = NibObjects.reuseIdentifierFor(.CompanyTableViewCell)
        let cell = tableView.dequeueReusableCellWithIdentifier(cellIdentifier, forIndexPath: indexPath) as! CompanyTableViewCell
        
        cell.configureCellWith(companies[indexPath.row])
        
        return cell
    }
    
    func tableView(tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat {
        return UITableViewAutomaticDimension
    }
    
}
