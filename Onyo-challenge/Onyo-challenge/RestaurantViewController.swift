//
//  RestaurantViewController.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/13/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit
import MapKit
import RealmSwift

class RestaurantViewController: UIViewController {

    // MARK: - Properties
    
    @IBOutlet var tableView: UITableView!
    
    var companies = [Company]()
    var categories = [Category]()
    
    // MARK: - Life Cycle
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        configContent()
        fetchCompanyList()
    }
    
    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(animated)
        
        configWithRealmData()
    }
    
    // MARK: - Configuration
    
    func configContent() {
        tableView.rowHeight = UITableViewAutomaticDimension
        tableView.estimatedRowHeight = 220.0
        
        navigationItem.config()
    }
    
    func configWithRealmData() {
        companies = Company.companiesFromRealm()
        categories = Category.categoriesFromRealm()
        tableView.reloadData()
    }
    
    // MARK: - API handlers
    
    func fetchCompanyList() {
        OnyoAPIManager.sharedInstance.fetchCompanyList({ (companies, categories) in
           self.deleteAllRealm()
            
            self.companies = companies
            for company in companies {
                company.save()
            }
            
            self.categories = categories
            for category in categories {
                category.save()
            }
            
            self.tableView.reloadData()
        }) { (error) in
        }
    }
    
    func deleteAllRealm() {
        let realm = try! Realm()
        realm.beginWrite()
        realm.deleteAll()
        try! realm.commitWrite()
    }
    
    // MARK: - Navigation
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "CategoriesSegue" {
            let destinationBar = segue.destinationViewController as! UITabBarController
            let destination = destinationBar.viewControllers![0] as! CategoryViewController
            destination.categories = categories
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
        
        let company = companies[indexPath.row]
        
        let openMap: () -> Void = { () in
            if let latitude = company.addressLatitude.value, let longitude = company.addressLongitude.value {
                let placemark = MKPlacemark(coordinate: CLLocation(latitude: latitude, longitude: longitude).coordinate, addressDictionary: nil)
                let item = MKMapItem(placemark: placemark)
                item.name = company.displayName
                item.openInMapsWithLaunchOptions(nil)
            }
        }
        
        cell.configureCellWith(company, indexPath: indexPath, openMap: openMap)

        return cell
    }
    
    func tableView(tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat {
        return UITableViewAutomaticDimension
    }
    
}

extension RestaurantViewController: UITableViewDelegate {
    
    func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
        performSegueWithIdentifier("CategoriesSegue", sender: self)
    }
    
}